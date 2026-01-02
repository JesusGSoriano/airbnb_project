-- models/staging/stg_reviews.sql
with source as (
    select *
    from public.raw_reviews
)

select
    id as review_id,
    listing_id,
    reviewer_id,
    reviewer_name,
    date::date as review_date,
    comments
from source