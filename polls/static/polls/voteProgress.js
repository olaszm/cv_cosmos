const totalVotes = JSON.parse(document.querySelector('#totalVotes').textContent)
const choices = JSON.parse(document.querySelector('#choices').textContent)
const progressBarElements = [...document.querySelectorAll('.progress-bar')]
const spanElements = [...document.querySelectorAll('.percentageEl')]

const setElementWidth = (el,width) => {
    el.style.width = `${+width}%`
} 

const calculatePercentage = (total,amount) => {
    return (+amount / total) * 100
}

progressBarElements.forEach((item,idx)=> {
    let w = calculatePercentage(totalVotes,choices[idx])
    spanElements[idx].textContent = `${w.toFixed(0)}%`
    item.setAttribute('aria-valuenow', w)
    setElementWidth(item,w)
})
