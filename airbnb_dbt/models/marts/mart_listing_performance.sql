with listings as (

    select
        listing_id,
        neighbourhood,
        room_type,
        price,
        availability_365,
        number_of_reviews,
        review_scores_rating
    from {{ ref('stg_listings') }}

),

reviews as (

    select
        listing_id,
        count(*) as total_reviews_comments
    from {{ ref('stg_reviews') }}
    group by listing_id

)

select
    l.listing_id,
    l.neighbourhood,
    l.room_type,
    l.price,
    l.availability_365,
    l.number_of_reviews,
    l.review_scores_rating,
    r.total_reviews_comments
from listings l
left join reviews r
    on l.listing_id = r.listing_id
