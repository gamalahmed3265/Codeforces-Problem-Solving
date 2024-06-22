var n = +readline()
var segments = readline().split` `.map(x => +x)


function can_form_triangle() {
    segments.sort((a,b)=>a-b);
    for (var i = 0; i < n-2; i++) {
        if(segments[i]+segments[i+1]>segments[i+2]){
            return "YES"
        }
    }    
    return "NO"
}

print(can_form_triangle())