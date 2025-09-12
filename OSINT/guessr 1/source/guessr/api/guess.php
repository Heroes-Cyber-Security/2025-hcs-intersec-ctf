<?php
header('Content-Type: application/json');

$raw = file_get_contents('php://input');
$data = json_decode($raw, true);
if (!$data || !isset($data['target_id']) || !isset($data['lat']) || !isset($data['lng'])) {
  echo json_encode([ 'success' => false, 'message' => 'Invalid payload' ]);
  exit;
}

$tid = intval($data['target_id']);
$plat = floatval($data['lat']);
$plng = floatval($data['lng']);

function read_secret($name, $fallback_env = null){
  $secret_path = "/run/secrets/" . $name;
  if (file_exists($secret_path)) {
    return trim(file_get_contents($secret_path));
  }
  if ($fallback_env !== null) {
    $from_env = getenv($fallback_env);
    if ($from_env !== false) return trim($from_env);
  }
  return null;
}

$targets = [
  1 => [
    'lat' => read_secret('target1_lat', 'TARGET1_LAT'),
    'lng' => read_secret('target1_lng', 'TARGET1_LNG'),
    'flag' => read_secret('flag1', 'FLAG1'),
  ],
  2 => [
    'lat' => read_secret('target2_lat', 'TARGET2_LAT'),
    'lng' => read_secret('target2_lng', 'TARGET2_LNG'),
    'flag' => read_secret('flag2', 'FLAG2'),
  ],
  3 => [
    'lat' => read_secret('target3_lat', 'TARGET3_LAT'),
    'lng' => read_secret('target3_lng', 'TARGET3_LNG'),
    'flag' => read_secret('flag3', 'FLAG3'),
  ],
];

if (!array_key_exists($tid, $targets) || $targets[$tid]['lat'] === null || $targets[$tid]['lng'] === null){
  echo json_encode([ 'success' => false, 'message' => 'Target tidak tersedia.' ]);
  exit;
}

function haversine($lat1, $lon1, $lat2, $lon2){
  $R = 6371000.0;
  $phi1 = deg2rad($lat1);
  $phi2 = deg2rad($lat2);
  $dphi = deg2rad($lat2 - $lat1);
  $dlambda = deg2rad($lon2 - $lon1);

  $a = sin($dphi/2)**2 + cos($phi1) * cos($phi2) * sin($dlambda/2)**2;
  $c = 2 * atan2(sqrt($a), sqrt(1 - $a));
  return $R * $c;
}

$radius_m = getenv('ACCEPT_RADIUS_M');
if ($radius_m === false || !is_numeric($radius_m)){
  $radius_m = 300; // default 300m
} else {
  $radius_m = floatval($radius_m);
}

$correct_lat = floatval($targets[$tid]['lat']);
$correct_lng = floatval($targets[$tid]['lng']);
$dist = haversine($plat, $plng, $correct_lat, $correct_lng);

if ($dist <= $radius_m){
  $flag = $targets[$tid]['flag'];
  if ($flag === null) $flag = 'Something error'; // fail‑safe default
  echo json_encode([ 'success' => true, 'flag' => $flag ]);
} else {
  echo json_encode([ 'success' => false, 'message' => 'Wrong answer!' ]);
}
