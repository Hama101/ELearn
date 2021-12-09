let g2s = document.getElementsByName('g2');
for (let i = 0 ; g2s.length ; i++){
    g2s[i].addEventListener('click' , function (e){
        e.preventDefault()
        let value = this.dataset.pk
        console.log(value);
        $.ajax({
            url:"http://127.0.0.1:8000/classes/setToAbsent/",
            data:{"pk":value},
            data_type:'json',
            success:function(res){
                console.log(res)
            },
        })
    })
}