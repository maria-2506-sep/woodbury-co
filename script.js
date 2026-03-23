// Smooth scrolling for navigation
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

e.preventDefault(); // VERY IMPORTANT

const name = document.querySelector("input[type=text]").value;
const email = document.querySelector("input[type=email]").value;
const guests = document.querySelector("input[type=number]").value;

// Send data to Flask backend
fetch("http://127.0.0.1:5000/add_reservation", {
method: "POST",
headers: {
"Content-Type": "application/json"
},
body: JSON.stringify({
name: name,
email: email,
guests: guests
})
})
.then(res => res.json())
.then(data => {
document.getElementById("responseMsg").innerText = data.message; // success message
form.reset(); // clear form
})
.catch(err => {
console.error(err);
document.getElementById("responseMsg").innerText = data.message;
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

const msg = document.getElementById("responseMsg");
msg.innerText = data.message;
msg.style.color = "green";

document.body.appendChild(popup);

});
});