const output = document.querySelector("#alert")
const contactForm = document.querySelector('#fruitkha-contact')
const inputName = document.querySelector('#email')
const message = document.querySelector('#message')


contactForm.addEventListener('submit', handleSubmit)

function handleSubmit(e) {
    e.preventDefault()
    if(inputName.value.length === 0){
        console.log('Empty');
        output.style.display = 'block'
        output.textContent = 'Email cannot be empty'
    }
    else if(message.value.length === 0){
        output.style.display = 'block'
        output.textContent = 'Please enter message'
        
    }else{
        output.style.display = 'none'
    }
}
