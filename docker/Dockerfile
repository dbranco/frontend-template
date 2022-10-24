FROM dbranco/cookiecutter:1.0.0

ENV HOST_USER_ID=0
ENV HOST_GROUP_ID=0

RUN apk add --update npm

ENTRYPOINT [ "cookiecutter", "gh:dbranco/frontend-template" ]