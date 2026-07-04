import json
import random

random.seed(7042026)

first_names = ["Mary","John","Lisa","Carlos","Nina","Rob","Angela","Derek","Megan","Tony","Patricia","Eric","Sofia","Ben","Tara","Victor","Grace","Sam","Paula","Omar","Kelly","Mark","Janet","Luis","Hannah","Rick","Dana","Eli","Monica","George","Priya","Steve","Laura","Kevin","Alicia","Brian","Wendy","Marcus","Jill","Ramon"]
last_names = ["Johnson","Miller","Garcia","Smith","Brown","Davis","Wilson","Anderson","Thomas","Moore","Martin","Lee","Clark","Lewis","Walker","Hall","Young","Allen","King","Wright","Scott","Green","Baker","Adams","Nelson","Hill","Ramirez","Campbell","Mitchell","Roberts"]
streets = ["River Rd","Maple St","Oak Ave","Pine Ct","Cedar Ln","Spruce Dr","Walnut Way","Elm St","Hickory Rd","Sycamore Blvd","Birch Terrace","Willow Dr","Poplar St","Chestnut Ct","Meadow Ln","Lakeview Dr"]
trees = ["oak","maple","pine","cedar","spruce","walnut","elm","hickory","sycamore","birch","willow","poplar"]
scopes = ["remove","trim","take down","cut down","prune","raise canopy on","remove and haul","deadwood"]
landmarks = ["near garage","by driveway","behind house","over fence","next to shed","by power line","front yard","back yard","near deck","leaning toward roof"]

def phone(i):
    return f"812-555-{1000+i:04d}"

def email_for(name, addrnum, i, typo=False):
    base = name.lower().replace(" ", ".")
    if typo:
        return f"{base}{addrnum} at gmail dot com"
    domains = ["gmail.com","yahoo.com","outlook.com","icloud.com"]
    return f"{base}{addrnum if i % 5 == 0 else ''}@{domains[i % len(domains)]}"

def price_base(tree_count, scope_i, bucket_i):
    return 650 + tree_count * 425 + (scope_i % 7) * 125 + (bucket_i % 9) * 50

def mk_options(p, kind, stump_extra=None):
    if kind == 1:
        return [{"label":"base work","scope":"tree work only","price":p}]
    if kind == 2:
        return [{"label":"option A","scope":"tree work only","price":p},{"label":"option B","scope":"tree work plus stump","price":p+500}]
    if kind == 3:
        return [{"label":"tree work","scope":"tree work only","price":p},{"label":"stump add-on","scope":"stump grinding add-on","price":stump_extra or 350}]
    return [{"label":"option 1","scope":"tree work and haul","price":p},{"label":"option 2","scope":"tree work, haul, and stump","price":p+650}]

def expected(first,last,ph,em,addrnum,street,count,tree,scope,landmark,options):
    return {
        "customer_name": f"{first} {last}",
        "phone": ph,
        "email": em.replace(" at ","@").replace(" dot ","."),
        "service_address": f"{addrnum} {street}",
        "tree_count": count,
        "tree_type": tree if count == 1 else tree + "s",
        "work_scope": scope,
        "location_notes": landmark,
        "options": options,
        "notes": ""
    }

def raw_easy(first,last,ph,em,addr,count,tree,scope,landmark,opts):
    opttext = "; ".join([f"{o['label']}: ${o['price']} ({o['scope']})" for o in opts])
    return f"{first} {last}, {ph}, {em}. {scope.capitalize()} {count} {tree}{'' if count==1 else 's'} at {addr} {landmark}. {opttext}."

def raw_medium(first,last,ph,em,addrnum,street,count,tree,scope,landmark,opts):
    ph2 = ph.replace("-","")
    opttext = " ".join([f"{o['label']} {o['price']} {o['scope']}" for o in opts])
    return f"{first.lower()} {last[0].lower()} {ph2} {em} {addrnum} {street.lower()} {scope} {count} {tree}{'' if count==1 else 's'} {landmark} {opttext}"

def raw_medium_messy(first,last,ph,em,addrnum,street,count,tree,scope,landmark,opts):
    ph2 = ph.replace("-","")
    opttext = " / ".join([f"{o['label'].replace('option ','opt')} maybe {o['price']} for {o['scope']}" for o in opts])
    typos = {"remove":"remve","trim":"trm","take down":"tak dwn","cut down":"cut dwn","prune":"prun","raise canopy on":"rase canopy","remove and haul":"rmv haul","deadwood":"dedwood"}
    sc = typos.get(scope, scope)
    return f"{first[:3].lower()} {last.lower()} {ph2} email {em} job {addrnum} {street.lower()} {sc} {count} {tree}{'' if count==1 else 's'} {landmark.replace('near','nr').replace('behind','bhnd')} price {opttext}"

def raw_messy_plus(first,last,ph,em,addrnum,street,count,tree,scope,landmark,opts):
    ph2 = ph[:3] + " " + ph[4:7] + " " + ph[8:]
    optbits = []
    for o in opts:
        optbits.append(f"{o['label'].replace('option ','op')} {o['price']} {o['scope'].replace('tree work','wrk').replace('stump grinding add-on','stmp')}")
    return f"{last.lower()}? no {first.lower()} {ph2} {addrnum} {street.lower()} {em} {tree} x{count} {scope.replace('take down','takedwn').replace('remove','rmv')} {landmark} {' or '.join(optbits)}"

def raw_uber(first,last,ph,em,addrnum,street,count,tree,scope,landmark,opts):
    phparts = ph.replace("-"," ")
    em2 = em.replace("@"," at ").replace("."," dot ")
    namefrag = f"{first[:2].lower()} maybe {first.lower()} {last[0].lower()}"
    opttext = " ".join([f"{o['label'][:3]} {o['price']} {o['scope'].split()[0]}??" for o in opts])
    return f"{namefrag} {phparts} no thats phone {em2} {street.split()[0].lower()} {addrnum} {street.split()[-1].lower()} {tree[:4]} {count}x {scope[:5]} {landmark.replace(' ','/')} {opttext}"

def raw_adversarial(first,last,ph,em,addrnum,street,count,tree,scope,landmark,opts):
    ph2 = ph.replace("-","")
    opttext = " ".join([f"{o['label']} {o['price']}" for o in opts])
    height = 25 + (addrnum % 35)
    return f"{first} {last} {ph2} {em} {addrnum} {street} {count} {tree}{'' if count==1 else 's'} {height} ft {scope} {landmark} {opttext} not phone not address prices are option nums"

buckets = [
    ("easy",50,raw_easy),
    ("medium",50,raw_medium),
    ("medium_messy",100,raw_medium_messy),
    ("messy_plus",100,raw_messy_plus),
    ("uber_messy",100,raw_uber),
    ("adversarial_number_confusion",100,raw_adversarial),
]

def build_records():
    records = []
    case_num = 1
    dataset_name = "td2_complete_cases_500_v1"
    for bucket, n, rawfn in buckets:
        for j in range(n):
            i = case_num
            first = first_names[(i*7+j) % len(first_names)]
            last = last_names[(i*5+j*3) % len(last_names)]
            ph = phone(i)
            addrnum = 100 + ((i*37) % 9800)
            street = streets[(i+j) % len(streets)]
            count = 1 + ((i+j) % 4)
            tree = trees[(i*3+j) % len(trees)]
            scope = scopes[(i+j*2) % len(scopes)]
            landmark = landmarks[(i*2+j) % len(landmarks)]
            p = price_base(count, scopes.index(scope), i)
            kind = 1 + (i+j) % 4
            opts = mk_options(p, kind, stump_extra=300+(i%6)*75)
            em = email_for(f"{first} {last}", addrnum, i, typo=(bucket == "uber_messy"))
            addr = f"{addrnum} {street}"
            if rawfn == raw_easy:
                raw = rawfn(first,last,ph,em,addr,count,tree,scope,landmark,opts)
            else:
                raw = rawfn(first,last,ph,em,addrnum,street,count,tree,scope,landmark,opts)
            records.append({
                "case_id": f"CC{case_num:04d}",
                "dataset_name": dataset_name,
                "messiness_bucket": bucket,
                "raw_input": raw,
                "expected": expected(first,last,ph,em,addrnum,street,count,tree,scope,landmark,opts)
            })
            case_num += 1
    return records

if __name__ == "__main__":
    records = build_records()
    with open("td2-complete-cases-500.jsonl", "w", encoding="utf-8") as f:
        for record in records:
            f.write(json.dumps(record, ensure_ascii=False, separators=(",",":")) + "\n")
    print(f"wrote {len(records)} records to td2-complete-cases-500.jsonl")
