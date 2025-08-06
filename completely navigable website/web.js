let i = 0;
let text = "HARE KRISHNA , Hello recruiters I am Mr.X a servant of Mr.Shiva Dubey wants to welcome you to the portfolio of him please navigate through the above given buttons for getting more details(buttons itself suggests their functions).";
let spd = 60;
function runTW() {
    if (i < text.length) {
        document.getElementById("para").innerHTML += text.charAt(i);
        i++;

        setTimeout(runTW, spd);
    }
}
window.onload = runTW;


