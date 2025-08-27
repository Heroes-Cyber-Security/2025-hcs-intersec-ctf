import sys, base64

def fix_padding(s: str) -> str:
    return s + "=" * (-len(s) % 4)

def decode_custom(encoded: str, rounds: int = 10) -> str:
    s = encoded.strip()
    for _ in range(rounds):
        s = base64.b64decode(fix_padding(s)).decode('latin-1')
    out = []
    for i in range(0, len(s), 4):
        chunk = s[i:i+4]
        if not chunk:
            continue
        try:
            ch = base64.b64decode(fix_padding(chunk)).decode('utf-8')
        except Exception:
            try:
                ch = base64.b64decode(fix_padding(chunk)).decode('latin-1')
            except Exception:
                ch = '?'
        out.append(ch)
    return ''.join(out)

if __name__ == "__main__":
    encoded = "Vm0wd2QyUXlWa1pPVldSWFYwZG9WRll3Wkc5V1ZteDBaRWhrVmxac2NEQlVWbHBQVm1zeFdHVkliRmhoTVhCUVZtcEdTMlJIVmtkaVJuQk9UVEJLU1ZadE1IaFRNVWw1Vkd0c2FWSnRVbGhVVkVaTFpWWmFkR05GU214U2JWSllWVzAxUzJGc1NuVlJiVGxhVjBoQ1dGcFdXbUZqTVZwMFVteHdWMDFWY0ZsV1Z6QXhWREpHYzFOdVVtaFNiWGhYVkZWYVlWUkdVblJsUjBacVRWZFNNRlZ0ZUc5aFZscHlWMVJDVjAxdVVuWldha1phWlZaT2NscEhjRk5pUlhCb1YxWlNSMWxXYkZkVmJGcFlZbGhTV0ZSV1dtRmxWbVJ5VjIxMFZXSkdjREZWVjNodlZqRktjMk5HYUZkaGEzQklWbXBHVDJSV1VuTmhSMnhvVFVoQ1dWWXhaREJaVjFGNFYxaG9WbUpIVWxsWmJGWmhWMFpzY2xwR1RrNVNia0pIVmpJeFIxWlhTa2RqUm1oYVRVWkthRlpxUm1Ga1JsWlZVV3hrYUdFeGNGVlhXSEJIWVRKU1YxWnVVbXhTYkVwVVZqQldTMlJzV25STldHUlZUVlZXTkZWc2FHOVdiVXB5VGxac1dtRXlhRVJaZWtaWFpFVTFWbFJzVWxkaVdGRjZWbXBLTUZReFdYZE5XRXBYWVdzMVlWUlZXbmRrYkZweFVtdHdiR0pWV2toWlZWcGhZa2RGZUdOR2JGZGlXRUpJV1ZSS1QyTXhaSFZVYkZacFZqTm9kbFpHV205Uk1sSnpWMjVPVm1Fd05XOVpXSEJYVmpGU1ZtRkhPVmRpUjFKSldWVmFjMWR0UlhoV1dHaFhUVlp3YUZwRlZYaFdWbEp5VGxkc1UwMHlaekZXYlhCTFRVZEZlRmRZWkU1WFJYQnhWVzB4TkZkV2JGVlNhM1JvVW14d2VGVnRNVWRXTURGeVRsVm9WMUo2UmtoV2FrWmhaRlpHYzFWc2FHbFNiSEI1Vm10U1IxTXhXWGhqUld4VVlYcHNXRmxZY0ZkV1ZscEhWV3QwYVUxWFVraFdNV2h2VjBkS1JrNVdUbFZXYkhBeldsWmFVMk14WkhSa1JtUk9ZVEZaTVZac1pEUmpNV1IwVTJ0a1ZHSnVRbGhWYTFaaFZrWmFjVkp0Um1waVZrcElWMnRrYzFVeVJYcFJiSEJYWVd0dmQxbHFSbEpsUm1SMVZXeFNhRTFzU25oV1YzaGhaREZaZUZkdVVteFNXRkpaVlcxNGQyVkdWblJrUkVKb1lYcEdXVlpYTlhOWFIwVjRZMFpvVjFJemFHaGFSbHBIWTJ4YWMxcEhhR2hOU0VKMlZtMTBVMU14VVhsVVdHaFdZbXhhVmxsclZURmpSbFp4VW10MFYxWnNjRmxhVldSSFlUSktWMUpxVWxkTmFsWlVXV3RhU21ReFpITmFSbkJwVW01Q1NWWkdVa2RWYlZaSFdraEthMUpzY0ZoWmEyaERVakZhVjFkc1RtcGlSVXBUVlVaUmQxQlJQVDA9"  

    flag = decode_custom(encoded, rounds=10)
    print(flag)
