# Proof of Concept
Jadi ges, kalian harus install [foundry](https://getfoundry.sh/) dulu. Lalu, hubungi web UI untuk challengenya.
Selesaikan captcha. Copy paste parameter yang muncul.

Kalian harus send transaksi yang memanggil fungsi `toggle()` di contract `Setup`

```sh
cast send $SETUP_ADDR 'toggle()' --private-key $PRIV --rpc-url $RPC_URL
```

Nanti dapet fleg
```
HCS{minat_belajar_blockchain?_hubungi_mas_hanz}
```
