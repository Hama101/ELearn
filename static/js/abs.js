let g1s = document.getElementsByName('g1');


for (let i = 0 ; g1s.length ; i++){
    g1s[i].addEventListener('click' , function (e){
        e.preventDefault()
        let value = this.dataset.pk
        console.log(value);
        $.ajax({
            url:"http://127.0.0.1:8000/classes/setToPresent/",
            data:{"pk":value},
            data_type:'json',
            success:function(res){
                console.log(res)
            },
        })
    })
}
