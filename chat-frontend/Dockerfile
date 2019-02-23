FROM node:8.10.0

WORKDIR /vue

RUN mkdir /vue/.npm-global
RUN npm config set prefix "/vue/.npm-global"
ENV PATH=~/.npm-global/bin:$PATH

COPY . /vue/

RUN npm install 

CMD ["npm", "build"]