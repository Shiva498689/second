let i = 0;
let text = " Please Welcome to BIODATA Of  Mr.Shiva Dubey";
let spd = 80;
function runTW() {
    if (i < text.length) {
        document.getElementById("para").innerHTML += text.charAt(i);
        i++;

        setTimeout(runTW, spd);
    }
}
window.onload = runTW;


