# Proof Of Concept

## TL;DR

There's a couple suspicious packets that uploaded a file named `read.php` that contains a PHP code reading a file named `flag.txt`
the flag is base64 encoded

`read.php` file:

```php
<?php
// read_flag.php - reads and displays the content of /flag.txt
$file_content = file_get_contents('/flag.txt');
echo "<pre>" . htmlspecialchars($file_content) . "</pre>";
?>
```

Encoded flag is:
`SENTe2thbGlhbl9sYW5nc3VuZ19maWx0ZXJfZmxhZ255YV9hdGF1X3BlcmhhdGlpbl9hcGFfYXR0YWNrZXJueWFfbGFrdWthbl9oZWhlfQ==`

Flag => `HCS{kalian_langsung_filter_flagnya_atau_perhatiin_apa_attackernya_lakukan_hehe}`
