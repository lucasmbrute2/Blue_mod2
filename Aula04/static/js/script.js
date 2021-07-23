const itens = document.querySelectorAll('.cores')


itens.forEach((item)=>{ /*aqui a sintaxe do FOR é diferente, sendo 'itens' a variável que nós criamos no começo do código, e 'item' a variável que irá iterar (varrer), ela pode ter qualquer nome, como no Python.*/
    item.addEventListener('click',() =>{

        if(item.style.textDecoration ==''){
            item.style.textDecoration = "line-through"
            item.style.backgroundColor = '#ccc'
            
        
        } else {
        
            item.style.textDecoration =''
            item.style.backgroundColor = '#fff'
        
        
        }

    })

})
    






