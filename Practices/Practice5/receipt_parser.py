
import re
import json
from decimal import Decimal

def parse_receipt(text: str) -> dict:
    result = {
        "store": {},
        "items": [],
        "totals": {},
        "payment": {},
        "metadata": {}
    }

    lines = [line.rstrip() for line in text.splitlines()]

    
    for line in lines:
        line = line.strip()
        if "Филиал" in line and "ТОО" in line:
            result["store"]["name"] = line.strip()
        if "БИН" in line:
            result["store"]["bin"] = line.split()[-1].strip()
        if "Чек №" in line:
            result["metadata"]["check_number"] = line.split("Чек №")[-1].strip()
        if "Касса" in line and "Смена" in line:
            parts = line.split()
            if len(parts) >= 4:
                result["metadata"]["cash_register"] = parts[1]
                result["metadata"]["shift"] = parts[3]

    
    dt_match = re.search(r'(\d{2}\.\d{2}\.\d{4})\s+(\d{2}:\d{2}:\d{2})', text)
    if dt_match:
        result["metadata"]["date"] = dt_match.group(1)
        result["metadata"]["time"] = dt_match.group(2)

    
    item_pattern = re.compile(
        r'^\s*(\d{1,2})\.\s+'
        r'(.+?)\s+'
        r'(\d+[,.\d]*)\s*[x×]\s+'
        r'(\d+[,.\d]+)\s+'
        r'(\d+[,.\d]+)\s*$',
        re.MULTILINE
    )

    items = []
    total_from_items = Decimal('0')

    for m in item_pattern.finditer(text):
        num, name, qty, price, subtotal = m.groups()

       
        name = name.replace('[RX]-', '').strip()

        
        qty = qty.replace(',', '.').strip()
        price = price.replace(',', '.').strip()
        subtotal = subtotal.replace(',', '.').strip()

        try:
            item = {
                "line": int(num),
                "name": name,
                "quantity": float(qty),
                "unit_price": float(price),
                "subtotal": float(subtotal)
            }
            items.append(item)
            total_from_items += Decimal(subtotal)
        except (ValueError, TypeError):
            continue

    result["items"] = items

   
    total_match = re.search(r'ИТОГО:\s*([\d\s,.]+)', text)
    if total_match:
        total_str = total_match.group(1).replace(' ', '').replace(',', '.')
        try:
            result["totals"]["total"] = float(total_str)
        except ValueError:
            result["totals"]["total"] = None

   
    nds_match = re.search(r'в т\.ч\. НДС 12%:\s*([\d\s,.]+)', text)
    if nds_match:
        nds_str = nds_match.group(1).replace(' ', '').replace(',', '.')
        try:
            result["totals"]["vat_12_percent"] = float(nds_str)
        except ValueError:
            result["totals"]["vat_12_percent"] = 0.0

    
    payment_block = False
    for line in lines:
        stripped = line.strip()
        if "Банковская карта:" in stripped:
            payment_block = True
            result["payment"]["method"] = "Банковская карта"
            continue
        if payment_block and stripped and re.match(r'^[\d\s,.]+$', stripped):
            amount_str = stripped.replace(' ', '').replace(',', '.')
            try:
                result["payment"]["amount"] = float(amount_str)
            except ValueError:
                pass
            payment_block = False
            break

    
    if "total" in result["totals"] and result["totals"]["total"] is not None:
        official = Decimal(str(result["totals"]["total"]))
        diff = abs(official - total_from_items)
        result["totals"]["items_sum"] = float(total_from_items)
        result["totals"]["difference"] = float(diff)

    return result


def print_receipt(parsed: dict):
    print("═" * 70)
    print(f"Магазин: {parsed['store'].get('name', '-')}")
    print(f"БИН:     {parsed['store'].get('bin', '-')}")
    print(f"Чек №:   {parsed['metadata'].get('check_number', '-')}")
    print(f"Дата:    {parsed['metadata'].get('date', '-')} {parsed['metadata'].get('time', '-')}")
    print("═" * 70)

    print(f"{'№':>3} {'Наименование':<44} {'Кол-во':>6} {'Цена':>9} {'Сумма':>10}")
    print("─" * 80)

    for item in parsed["items"]:
        name = item["name"][:42] + "..." if len(item["name"]) > 42 else item["name"]
        print(f"{item['line']:>3} {name:<44} {item['quantity']:>6.0f} "
              f"{item['unit_price']:>9,.0f} {item['subtotal']:>10,.0f}")

    print("─" * 80)

    items_sum = sum(i["subtotal"] for i in parsed["items"])
    print(f"Сумма по позициям:          {items_sum:>14,.0f}")
    if "total" in parsed["totals"] and parsed["totals"]["total"]:
        print(f"Итого по чеку:              {parsed['totals']['total']:>14,.0f}")
    if "difference" in parsed["totals"] and parsed["totals"]["difference"] > 0.01:
        print(f"Разница:                    {parsed['totals']['difference']:>14,.2f}")
    if "vat_12_percent" in parsed["totals"]:
        print(f"в т.ч. НДС 12%:             {parsed['totals']['vat_12_percent']:>14,.0f}")

    print("═" * 70)
    if "payment" in parsed and "amount" in parsed["payment"]:
        print(f"Оплата: {parsed['payment']['method']} {parsed['payment']['amount']:,.0f}")
    print("═" * 70)


if __name__ == "__main__":
    try:
        with open("raw.txt", encoding="utf-8") as f:
            receipt_text = f.read()
    except FileNotFoundError:
        print("Файл raw.txt не найден в текущей папке!")
        exit(1)

    parsed = parse_receipt(receipt_text)

    print_receipt(parsed)

   
    with open("parsed_receipt.json", "w", encoding="utf-8") as f:
        json.dump(parsed, f, ensure_ascii=False, indent=2)
