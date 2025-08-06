let i = 0;
let text = "SCHOOLING INFO OF SHIVA DUBEY";
let spd = 80;
function runTW() {
    if (i < text.length) {
        document.getElementById("para").innerHTML += text.charAt(i);
        i++;

        setTimeout(runTW, spd);
    }
}
window.onload = runTW;
