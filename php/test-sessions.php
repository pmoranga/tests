<?php
$OUT="";
$cookie[0]="";

function gimme200(){
  $r = "";
  for ($i=0;$i<200;$i++) 
    $r = $r."a";
  return $r;
}

$max=3;
for ($i=0;$i<$max;$i++){
  if (isset($_COOKIE["PEDRO$i"])){
    $cookie[$i]=$_COOKIE["PEDRO$i"];
    $OUT=$OUT. "cookie PEDRO$i has => ".strlen($cookie[$i]) ." bytes\n\n";
  }
  $cookie[$i]=$cookie[$i] . gimme200();
  $OUT = $OUT. "setting PEDRO$i => ". strlen($cookie[$i]) ." bytes\n\n";
  setcookie("PEDRO$i",$cookie[$i],time()+3600);
}
print $OUT;



?>
