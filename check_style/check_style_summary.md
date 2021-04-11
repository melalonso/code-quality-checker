## CLI Relevant arguments 

### Checks to apply

```
-c configurationFile
```
[Required] Specifies the location of the file that defines the configuration modules.	

You can also run a single rule by referencing it using its category and name (more details here). 
For example, you can check for unnecessary modifiers on Java sources with -R category/java/codestyle.xml/UnnecessaryModifier.

### Format

```
-f format
```

Specifies the output format. Valid values: xml, plain, for XMLLogger and DefaultLogger respectively. Defaults to plain.

##### Plain
```
[WARN] /Users/melvin.elizondo/Documents/tesis/repos/elasticsearch/test/framework/src/main/java/org/elasticsearch/cluster/ESAllocationTestCase.java:298: Line is longer than 100 characters (found 134). [LineLength]
[WARN] /Users/melvin.elizondo/Documents/tesis/repos/elasticsearch/test/framework/src/main/java/org/elasticsearch/cluster/ESAllocationTestCase.java:298:17: 'if' child has incorrect indentation level 16, expected level should be 8. [Indentation]
```

##### XML
```
<file name="/Users/melvin.elizondo/Documents/tesis/repos/java-design-patterns/filterer/pom.xml"></file>
<file name="/Users/melvin.elizondo/Documents/tesis/repos/java-design-patterns/filterer/src/test/java/com/iluwatar/filterer/threat/SimpleThreatAwareSystemTest.java">
	<error line="28" column="1" severity="warning" message="Extra separation in import group before &apos;java.util.List&apos;" source="com.puppycrawl.tools.checkstyle.checks.imports.CustomImportOrderCheck"/>
	<error line="28" column="1" severity="warning" message="Wrong lexicographical order for &apos;java.util.List&apos; import. Should be before &apos;org.junit.jupiter.api.Test&apos;." source="com.puppycrawl.tools.checkstyle.checks.imports.CustomImportOrderCheck"/>
	<error line="30" column="1" severity="warning" message="Import statement for &apos;org.junit.jupiter.api.Assertions.*&apos; is in the wrong order. Should be in the &apos;STATIC&apos; group, expecting not assigned imports on this line." source="com.puppycrawl.tools.checkstyle.checks.imports.CustomImportOrderCheck"/>
	<error line="30" column="47" severity="warning" message="Using the &apos;.*&apos; form of import should be avoided - org.junit.jupiter.api.Assertions.*." source="com.puppycrawl.tools.checkstyle.checks.imports.AvoidStarImportCheck"/>
</file>
```

### Output 

```
-o file
```

Sets the output file. Defaults to stdout.


### Properties

```
-p propertiesFile
```

Sets the property files to load.

### Help

```
-h, --help
```

Print usage help message and exit. Any other option is ignored.
