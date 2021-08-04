<?php

$emp=[
    [1,"Animesh","devloper"],
    [2,"satyam","ethical hacker"],
    [3,"Anand","ethical hacker"]
];
for($row = 0;$row<3;$row++){
    for($col = 0;$col <3 ; $col++){
        echo $emp[$row][$col]."  ";
    }
    echo"<br>";
}
echo "<pre>";
print_r($emp ) . "<br>";
echo "</pre>";
?>
