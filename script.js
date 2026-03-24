// Smooth scrolling for navigation
console.log("JS CONNECTED");
document.addEventListener("DOMContentLoaded", function () {

// ------------------ SMOOTH SCROLL ------------------
document.querySelectorAll("nav a").forEach(link => {
link.addEventListener("click", function(e){

const targetId = this.getAttribute("href");

if(targetId.startsWith("#")){
e.preventDefault();

document.querySelector(targetId).scrollIntoView({
behavior: "smooth"
});
}

});
});


// ------------------ FORM SUBMISSION ------------------
const form = document.querySelector("form");

if(form){
form.addEventListener("submit", function(e){

e.preventDefault();

const name = document.getElementById("name").value;
const email = document.getElementById("email").value;
const guests = document.getElementById("guests").value;

fetch("http://localhost:5000/add_reservation", {
method: "POST",
headers: {
"Content-Type": "application/json"
},
body: JSON.stringify({ name, email, guests })
})
.then(res => res.json())
.then(data => {
const msg = document.getElementById("responseMsg");
msg.innerText = data.message;
msg.style.color = "green";
msg.style.fontWeight = "bold";
form.reset();
})
.catch(err => {
console.error(err);
document.getElementById("responseMsg").innerText = "Something went wrong ❌";
});

});
}



// ------------------ GALLERY IMAGE POPUP ------------------
const images = document.querySelectorAll(".gallery img");

images.forEach(img => {
img.addEventListener("click", function(){

const popup = document.createElement("div");

popup.style.position = "fixed";
popup.style.top = "0";
popup.style.left = "0";
popup.style.width = "100%";
popup.style.height = "100%";
popup.style.background = "rgba(0,0,0,0.8)";
popup.style.display = "flex";
popup.style.justifyContent = "center";
popup.style.alignItems = "center";

const popupImg = document.createElement("img");
popupImg.src = this.src;
popupImg.style.maxWidth = "80%";
popupImg.style.borderRadius = "10px";

popup.appendChild(popupImg);

// click anywhere to close
popup.addEventListener("click", function(){
popup.remove();
});

document.body.appendChild(popup);

});
});
});