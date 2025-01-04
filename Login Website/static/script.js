const formbox = document.querySelector(".formbox");
const loglink = document.querySelector(".loglink");
const reglink = document.querySelector(".reglink");

reglink.addEventListener("click", () => {
  formbox.classList.add("active");
});

loglink.addEventListener("click", () => {
    formbox.classList.remove("active");
  });

