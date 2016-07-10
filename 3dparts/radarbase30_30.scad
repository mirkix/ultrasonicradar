difference() {
    $fn = 120;
    cylinder(h= 30, r = 30/2);
    cylinder(h= 30, r = 28/2);    
    translate([0,0,8]) {
        rotate(a=[0,90,0]) {
            $fn = 120;
            cylinder(h= 20, r = 5);
        }
    }
}
