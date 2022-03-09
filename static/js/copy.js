const copyBtns = [...document.getElementsByClassName('copy-btn')]

let previous = null

copyBtns.forEach(btn => btn.addEventListener('click', ()=>{
  const imageUrl = btn.getAttribute('data-cp')
  navigator.clipboard.writeText(imageUrl)
  btn.textContent = 'copied'

  if (previous) {
    previous.textContent = 'Copy Image Link'
  }

  previous = btn
}))