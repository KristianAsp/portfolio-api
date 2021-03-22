package com.aspevik.portfolioapi.projects.application;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.aspevik.portfolioapi.projects.repository.ProjectRepository;

@Service
public class ProjectService {

    @Autowired
    private ProjectRepository projectRepository;

    public List<ProjectEntity> list() {
        return projectRepository.findAll();
    }
}
