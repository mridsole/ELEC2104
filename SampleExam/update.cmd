@echo off
cd /d E:/python/elec2104/SampleExam
jupyter nbconvert --to html SampleExam.ipynb
jupyter nbconvert --to html SampleExamSOlutions.ipynb
@echo on
cd ../
git add SampleExam/*
git commit -m "updated exam and solutions"
git push origin gh-pages