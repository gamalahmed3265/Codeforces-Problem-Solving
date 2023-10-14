<?php

function sumNumbers($X, $Y) {
    return $X + $Y;
}

// Read input from standard input
$handle = fopen("php://stdin", "r");

$input = trim(fgets($handle));

list($X, $Y) = explode(' ', $input);
$X = intval($X);
$Y = intval($Y);

$result = sumNumbers($X, $Y);
echo $result."\n";


fclose($handle);
