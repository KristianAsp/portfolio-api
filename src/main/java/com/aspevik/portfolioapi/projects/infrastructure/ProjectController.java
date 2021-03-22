package com.aspevik.portfolioapi.projects.infrastructure;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.aspevik.portfolioapi.projects.application.ProjectEntity;
import com.aspevik.portfolioapi.projects.application.ProjectService;

@RestController
@RequestMapping("/api")
public class ProjectController {

    @Autowired
    ProjectService projectService;

    @GetMapping(value = "/project/{projectId}")
    public List<ProjectEntity> get(@PathVariable String projectId){
        List<ProjectEntity> projects = projectService.list();
        return projects;
    }
}
