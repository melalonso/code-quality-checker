## CLI Relevant arguments 

### RuleSets

```
-rulesets <refs>
-R <refs>
```
[Required] Comma-separated list of ruleset or rule references.	

You can also run a single rule by referencing it using its category and name (more details here). 
For example, you can check for unnecessary modifiers on Java sources with -R category/java/codestyle.xml/UnnecessaryModifier.	

### Directory

```
-dir <path>
-d <path>
```
[Required] Root directory for the analyzed sources.		

### FileList

```
-filelist <filepath>
```

Path to file containing a comma delimited list of files to analyze. If this is given, then you don't need to provide -dir.		

### Language

```
-language <lang>
```

Specify the language PMD should use. Used together with -version. See also Supported Languages.

```
-language java -version 8
```

### Format

```
-format <format>
-f <format>
```

Output format of the analysis report. Some of them are:

CSV
```
"Problem","Package","File","Priority","Line","Description","Rule set","Rule"
"1","net.sourceforge.pmd","/home/pmd/source/pmd-core/src/main/java/net/sourceforge/pmd/RuleContext.java","2","124","Logger calls should be surrounded by log level guards.","Best Practices","GuardLogStatement"
"1","net.sourceforge.pmd.benchmark","/home/pmd/source/pmd-core/src/main/java/net/sourceforge/pmd/benchmark/Benchmarker.java","3","58","This for loop can be replaced by a foreach loop","Best Practices","ForLoopCanBeForeach"
```

json
```
{
  "formatVersion": 0,
  "pmdVersion": "6.24.0",
  "timestamp": "2021-02-21T17:17:52.648-06:00",
  "files": [
    {
      "filename": "/Users/melvin.elizondo/Documents/UNIVERSIDAD/TESIS/code-quality-checker/repos/elasticsearch/buildSrc/src/main/java/org/elasticsearch/gradle/DependenciesGraphTask.java",
      "violations": [
        {
          "beginline": 110,
          "begincolumn": 13,
          "endline": 110,
          "endcolumn": 25,
          "description": "Substitute calls to size() \u003d\u003d 0 (or size() !\u003d 0, size() \u003e 0, size() \u003c 1) with calls to isEmpty()",
          "rule": "UseCollectionIsEmpty",
          "ruleset": "Best Practices",
          "priority": 3,
          "externalInfoUrl": "https://pmd.github.io/pmd-6.24.0/pmd_rules_java_bestpractices.html#usecollectionisempty"
        }
      ]
    }
  ],
  "suppressedViolations": [],
  "processingErrors": [],
  "configurationErrors": []
}
```

### Report File

```
-reportfile <path>
-r <path>
```

Path to a file in which the report output will be sent. By default the report is printed on standard output.

### Short Names

```
-shortnames	
```

Prints shortened filenames in the report.