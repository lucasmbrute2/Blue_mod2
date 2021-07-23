const itens = document.querySelectorAll('.itens')
let botao = document.querySelector('#mudarPagina')


itens.forEach((item)=>{
    item.addEventListener('click',() =>{

        if(item.style.textDecoration ==""){
            item.style.textDecoration = "line-through"
            item.style.backgroundColor = '#ccc'
            
        
        } else {
        
                item.style.textDecoration =''
                item.style.textDecoration = '#fff'
        
        
        }

    })

})
    






