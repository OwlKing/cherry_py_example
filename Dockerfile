FROM arturosaco/cherrypy_server_base_image

EXPOSE 443

RUN git clone https://github.com/indexds/cherry_py_example
CMD python cherry_py_example/aux_clone_repo.py && cd cherrypy_server && python cherrypy_server.py




