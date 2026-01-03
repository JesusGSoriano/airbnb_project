-- models/staging/stg_listings.sql
with source as (
    select *
    from public.raw_listings
    where id is not null
)

select
    id as listing_id,
    host_id,
    neighbourhood_cleansed as neighbourhood,
    neighbourhood_group_cleansed as district,
    latitude,
    longitude,
    property_type,
    room_type,
    accommodates,
    bedrooms,
    beds,
    bathrooms_text as bathrooms,
    cast(replace(replace(price, '$',''), ',', '') as numeric) as price,
    minimum_nights,
    availability_365,
    number_of_reviews,
    reviews_per_month,
    review_scores_rating
from source
