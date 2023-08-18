Select 
	industry, count(*)  as contador, 
	min(imdb_rating) as minimo, 
    max(imdb_rating) as maximo, 
    round(avg(imdb_rating), 2) as promedio
from movies
group by industry;

select release_year, count(*) as movies_count
from movies
group by release_year 
having movies_count > 2
order by movies_count desc;

Select name, year(curdate()) - birth_year as edad From actors;

