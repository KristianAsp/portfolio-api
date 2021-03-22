package com.aspevik.portfolioapi.projects.infrastructure;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/api")
public class ProjectController {

    @GetMapping(value = "/project/{projectId}")
    public String get(@PathVariable String projectId){
        return projectId;
    }
}
