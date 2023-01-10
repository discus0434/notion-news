docker run -it \
    --name notion-news \
    --runtime nvidia \
    --gpus all \
    --env-file .env  \
    -d \
    --restart always \
    notion-news:latest /bin/bash
