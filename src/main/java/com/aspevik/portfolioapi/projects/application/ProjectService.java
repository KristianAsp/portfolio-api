package com.aspevik.portfolioapi.projects.application;

import java.util.List;
import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.stereotype.Service;
import org.springframework.web.bind.annotation.ResponseStatus;

import com.aspevik.portfolioapi.projects.repository.ProjectRepository;

@Service
public class ProjectService {

    @Autowired
    private ProjectRepository projectRepository;

    public List<ProjectEntity> list() {
        return projectRepository.findAll();
    }

    public List<ProjectEntity> findByName(String projectName) {
        return projectRepository.findByName(projectName);
    }

    public Optional<ProjectEntity> findById(Integer projectId) {
        Optional<ProjectEntity> optionalProjectEntity = projectRepository.findById(projectId);
        return optionalProjectEntity;
    }

}
