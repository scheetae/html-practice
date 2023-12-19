const line = document.querySelector(".line")
const items = document.querySelectorAll("span")
const container = document.querySelector(".container")


const getWidthFrom = (item) => {
  return item.getBoundingClientRect().width;
};

const getLeftFrom = (item) => {
  return item.getBoundingClientRect().left;
};

items.forEach(item => {
  item.addEventListener("click", () => {
    const itemWidth = getWidthFrom(item)
    const itemLeft = getLeftFrom(item)

    line.style.left = itemLeft - 8 + "px";
    line.style.width = itemWidth + "px";
  })
});
