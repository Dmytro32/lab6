# lab5
1. Use Makefile
2. Clean everything with make docker-prune
3. Create  push images
```
docker-push: 
	@docker push$(REPO): app \ 
	&& docker push $(REPO):tests
```
4. Create rule for delete images
```
images-delete: @sudo docker image rm --force $(shell sudo docker images -q)
```
5. Create and run docker-compose
```
sudo docker-compose up
```
6. localhost:80 work
7. Stop docker-compose 
```
sudo docker-compose down
```
8. Push docker-compose to Docker
9. Create docker for lab4 and push in it's repositoriy
