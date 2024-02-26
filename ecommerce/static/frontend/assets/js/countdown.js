const eventBox = document.querySelector('#event-box')
console.log(eventBox.textContent)

const countdownDays = document.getElementById('countdown-box')
const countdownHour = document.getElementById('countdown-box1')
const countdownMins = document.getElementById('countdown-box2')
const countdownSecs = document.getElementById('countdown-box3')

const eventDate = Date.parse(eventBox.textContent)
console.log(eventDate)

setInterval(()=>{
    const now = new Date().getTime()

    // console.log(now)

    const diff = eventDate - now 
    // console.log(diff)
    const day = Math.floor(eventDate/(1000 * 60 * 60 * 24) - (now / (1000 * 60 * 60 * 24)))
    // console.log(day)
    const hour = Math.floor((eventDate/(1000 * 60 * 60) - (now / (1000 * 60 * 60))) % 24)
    // console.log(hour)
    const mins = Math.floor((eventDate/(1000 * 60) - (now / (1000 * 60))) % 60)
    // console.log(mins)
    const secs = Math.floor((eventDate/(1000) - (now / (1000))) % 60)
    // console.log(secs)

    if (diff > 0){
        countdownDays.innerHTML  = day;
        countdownHour.innerHTML  = hour;
        countdownMins.innerHTML  = mins;
        countdownSecs.innerHTML  = secs;
    } else{

    }
}, 1000)





