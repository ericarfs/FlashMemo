const nxtBtn = [...document.querySelectorAll('.next-btn')];
const preBtn = [...document.querySelectorAll('.prev-btn')];
const productContainers = [...document.querySelectorAll('.item-list')];

const itemWidth = 200
const padding = 10

productContainers.forEach((item, i) => {
    let containerDimensions = item.getBoundingClientRect();
    let containerWidth = containerDimensions.width;

    nxtBtn[i].addEventListener('click', () => {
        item.scrollLeft += itemWidth + padding
    })

    preBtn[i].addEventListener('click', () => {
        item.scrollLeft -= itemWidth + padding
    })
})


function flipCard(elem) {
    if(elem.classList.contains('flipped'))   elem.classList.remove('flipped');
    else elem.classList.add('flipped');
}
