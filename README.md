# YouTube fetcher API

an API to fetch latest videos sorted in reverse chronological order of their publishing date-time from YouTube for a given tag/search query in a paginated response.

## Start Server

Make sure to populate the enviroment variables from `.env.local` into a `.env` file

Then, from the project's root, run:

```
docker-compose up -d --build
```

## Endpoints

```
GET /videos/

Query Parameters: {
  page: string
  search: string
}

```

### Response Schema

```
{
  count: number,
  next: string | null
  previous: string | null
  results: {
    title: string, 
    description: string, 
    published_on: string, 
    thumbnail_url: string, 
    video_url: string
  }[]
}
```
