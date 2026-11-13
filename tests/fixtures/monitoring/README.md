# Offline monitoring fixtures

These small, stored synthetic admissions pages and recorded HTTP response shapes test the monitor. They are not evidence about any real university. The PDF is a fixed one-page test document. Tests inject these files as HTTP responses and prohibit live requests.

The variants isolate navigation/cookie/footer changes, a one-digit tuition change, and a new academic-cycle marker. HTTP fixtures cover redirects, 404, a challenge wall and Retry-After. Robots fixtures include a wildcard, an anchored query rule, an Allow exception and Crawl-delay.
