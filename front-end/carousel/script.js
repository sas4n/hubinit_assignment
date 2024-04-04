import axios from "axios";

const imageLinks = [
  "https://cdn.mos.cms.futurecdn.net/dP3N4qnEZ4tCTCLq59iysd.jpg",
  "https://i.redd.it/tc0aqpv92pn21.jpg",
  "https://wharferj.files.wordpress.com/2015/11/bio_north.jpg",
  "https://images7.alphacoders.com/878/878663.jpg",
  "https://theawesomer.com/photos/2017/07/simon_stalenhag_the_electric_state_6.jpg",
  "https://da.se/app/uploads/2015/09/simon-december1994.jpg",
];
document.addEventListener("DOMContentLoaded", async (e) => {
  const itemTemplate = document.querySelector("#item-template");

  const slider = document.querySelector(".slider");

  const { data } = await axios.get("http://localhost:8000/api/blogs/");
  data.forEach((item, index) => {
    const itemClone = itemTemplate.content.cloneNode(true);
    itemClone.querySelector(".item").style.backgroundImage = `url(${
      imageLinks[index % imageLinks.length]
    })`;
    itemClone.querySelector(".title").textContent = item.blog_title;
    itemClone.querySelector(".description").textContent = item.blog_text;
    itemClone.querySelector(".status").textContent = item.status;
    slider.appendChild(itemClone);
  });
  console.log(data);
});
const slider = document.querySelector(".slider");

function activate(e) {
  const items = document.querySelectorAll(".item");
  e.target.matches(".next") && slider.append(items[0]);
  e.target.matches(".prev") && slider.prepend(items[items.length - 1]);
}

document.addEventListener("click", activate, false);
