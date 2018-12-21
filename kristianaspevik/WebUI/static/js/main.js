function applyFilters(){
    var resultSet = $('.projectCards .card'); //Obtain all projects.

    var filters = $('.filter');

    filters.each(function(){
        var filtersToBeApplied = []
        var filterID = this.id

        $('#' + filterID + ' option').each(function(){
            if (this.selected == true){
            filtersToBeApplied.push(this.innerHTML)
            }
        })
        var filter = ":has("

        for(var i = 0; i < filtersToBeApplied.length; i++){
            if(i > 0){
                filter += ","
            }
            filter += 'a[data-filter=\"' + filtersToBeApplied[i] +'\"]'
        }

        filter += ')'
        if(filter != ":has()"){
            resultSet = resultSet.filter(filter)
        }
    })
    showAndHideResult(resultSet)
}

function showAndHideResult(resultSet){
    var fullSet = $('.projectCards .card'); //Obtain all projects.
    fullSet.each(function(){
        $(this).hide()
    })

    resultSet.each(function(){
        $(this).show()
    })
}
