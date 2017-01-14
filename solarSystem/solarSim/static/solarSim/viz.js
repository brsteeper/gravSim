function plot(planet)
{
    var nameText = "Planet name is ";
    d3.select("body").append("p")
        .text(nameText)
        .append()
        .text(planet.name);

    //console.log(planet)
    d3.select("body").append("br");
    var planetX = planet.x;
    var planetY = -planet.y; //because d3's coordinates run top to bottom. Thus, invert it for users

    var svgWidth = 300;
    var svgHeight = svgWidth;

    //Scale planet coordinates down to SVG coordinates
    /*var maxCoord = Math.max(planetX, planetY);
    var edgeGuard = Math.max(svgWidth, svgHeight)/1.2; //make sure the coordinates are well inside the container
    var scale = edgeGuard/maxCoord; 
    var newX = planetX*scale;
    var newY = planetY*scale;*/


    var absMax = Math.max(Math.abs(planetX),Math.abs(planetY));
    var quadrMax = Math.sqrt((planetX*planetX)+(planetY*planetY)); //find the starting distance from sun
    var adjMax = quadrMax*1.15;  //make sure the planet is in from the edge
    var negMax = -adjMax;

    var linearScale = d3.scaleLinear()
        .domain([negMax, adjMax])
        .range([0, svgWidth]);

    var newX = linearScale(planetX);
    var newY = linearScale(planetY);

    var planetR = 3;
    var Xtext = "Planet X is ";
    var Ytext = "Planet Y is ";
    d3.select("body").append("p")
        .text(Xtext)
        .append()
        .text(newX);
    d3.select("body").append("br");
    d3.select("body").append("p")
        .text(Ytext)
        .append()
        .text(newY);

     d3.select("body").append("br");

    var sunCX = svgWidth/2;
    var sunCY = svgHeight/2;
    var sunR = 3;


    var svgElement = d3.select("body").append("svg")
        .attr("width", svgWidth)
        .attr("height", svgHeight)
        .style("border", "1px solid black");

    var Sun = svgElement.append("circle")
        .attr("cx", sunCX)
        .attr("cy", sunCY)
        .attr("r", sunR)
        .style("fill", "orange");
    
    var planet = svgElement.append("circle")
        .attr("cx", newX)
        .attr("cy", newY)
        .attr("r", planetR)
        .style("fill", "brown");
}