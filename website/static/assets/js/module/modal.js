// Script para o controle de modais
(() => {
    const modais = document.querySelectorAll('[data-modal]')
    const botoesAbrir = document.querySelectorAll('[data-modal-abrir]')
    
    modais.forEach((modal) => {
        modal.addEventListener('click', (evento) => {
            if(evento.target === modal)
                modal.close()
        })

        if(modal.classList.contains('modal--aberto'))
            modal.showModal()
    })

    botoesAbrir.forEach((botao) => {
        const atributo = botao.dataset.modalAbrir
        const modal = document.querySelector(`[data-modal="${atributo}"]`)

        botao.addEventListener('click', (evento) => {
            evento.preventDefault()
            modal.showModal()
        })
    })
})

()