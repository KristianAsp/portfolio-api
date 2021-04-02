package com.aspevik.portfolioapi.projects.repository;

import java.util.List;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import com.aspevik.portfolioapi.projects.application.ProjectEntity;

@Repository
public interface ProjectRepository extends JpaRepository<ProjectEntity, Integer> {
    List<ProjectEntity> findByName(String projectName);
}
