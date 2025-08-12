FROM oven/bun:1

RUN apt-get update && apt-get install -y npm && rm -rf /var/lib/apt/lists/*
RUN groupadd -r ctf && useradd -r -g ctf ctf
WORKDIR /home/ctf
COPY --chown=ctf:ctf package.json ./
RUN bun install
COPY --chown=ctf:ctf . .
RUN bun run build && rm -rf node_modules/@next/swc-* && rm -rf /tmp/*
RUN cp -r .next/static .next/standalone/.next/
RUN cp -r public .next/standalone/
RUN chown -R ctf:ctf /home/ctf/node_modules
RUN mkdir -p /home/ctf/.cache && chown -R ctf:ctf /home/ctf/.cache

USER ctf
WORKDIR /home/ctf/.next/standalone
EXPOSE 10001 50032
ENV PORT=10001
CMD ["sh", "-c", "cd /home/ctf && bun run server/index.ts & sleep 3 && cd /home/ctf/.next/standalone && node server.js"]
