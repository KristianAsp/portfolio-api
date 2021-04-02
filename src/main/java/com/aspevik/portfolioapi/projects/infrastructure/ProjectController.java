package com.aspevik.portfolioapi.projects.infrastructure;

import java.util.List;
import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseStatus;
import org.springframework.web.bind.annotation.RestController;

import com.aspevik.portfolioapi.projects.application.ProjectEntity;
import com.aspevik.portfolioapi.projects.application.ProjectService;

@RestController
@RequestMapping("/api")
public class ProjectController {

    @Autowired
    ProjectService projectService;

    @GetMapping(value = "/project/")
    public List<ProjectEntity> get(){
        List<ProjectEntity> projects = projectService.list();
        return projects;
    }

    @GetMapping(value = "/project/{projectId}")
    public ProjectEntity get(@PathVariable Integer projectId){
        Optional<ProjectEntity> optionalProjectEntity = projectService.findById(projectId);

        if(optionalProjectEntity.isEmpty()) {
            throw new ProjectNotFoundException();
        }

        return optionalProjectEntity.get();
    }

    @ResponseStatus(code = HttpStatus.NOT_FOUND, reason = "Project not found")
    private static class ProjectNotFoundException extends RuntimeException {}
}
