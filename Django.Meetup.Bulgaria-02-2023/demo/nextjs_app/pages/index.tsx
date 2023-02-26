import Head from 'next/head'
import styles from '@/styles/Home.module.css'
import ComponentWithFetch from 'components/ComponentWithFetch';

export default function Home() {
  return (
    <>
      <Head>
        <title>Create Next App</title>
        <meta name="description" content="Generated by create next app" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <main className={styles.main}>
        <h1 className={styles.heading}>Django Meetup Bulgaria 27.02.2022</h1>
        <div className={styles.row}>
          <ComponentWithFetch crud={[10, 10, 1, 1]} />
          <ComponentWithFetch crud={[2, 10, 1, 1]} />
          <ComponentWithFetch crud={[3, 10, 1, 1]} />
          <ComponentWithFetch crud={[4, 10, 1, 1]} />
        </div>
        <div className={styles.row}>
          <ComponentWithFetch crud={[10, 10, 0, 0]} />
          <ComponentWithFetch crud={[10, 2, 0, 0]} />
          <ComponentWithFetch crud={[10, 3, 0, 0]} />
          <ComponentWithFetch crud={[10, 4, 0, 0]} />
        </div>
        <div className={styles.row}>
          <ComponentWithFetch crud={[10, 10, 0, 0]} />
          <ComponentWithFetch crud={[10, 10, 0, 0]} />
          <ComponentWithFetch crud={[10, 10, 0, 0]} />
          <ComponentWithFetch crud={[10, 10, 0, 0]} />
        </div>
        <div className={styles.row}>
          <ComponentWithFetch crud={[10, 10, 0, 0]} />
          <ComponentWithFetch crud={[10, 10, 0, 0]} />
          <ComponentWithFetch crud={[10, 10, 0, 0]} />
          <ComponentWithFetch crud={[10, 10, 0, 0]} />
        </div>
        <div className={styles.row}>
          <ComponentWithFetch crud={[10, 2, 0, 0]} />
          <ComponentWithFetch crud={[2, 2, 0, 0]} />
          <ComponentWithFetch crud={[3, 2, 0, 0]} />
          <ComponentWithFetch crud={[4, 2, 0, 0]} />
        </div>
        <div className={styles.row}>
          <ComponentWithFetch crud={[2, 10, 0, 0]} />
          <ComponentWithFetch crud={[2, 2, 0, 0]} />
          <ComponentWithFetch crud={[2, 3, 0, 0]} />
          <ComponentWithFetch crud={[2, 4, 0, 0]} />
        </div>
        <div className={styles.row}>
          <ComponentWithFetch crud={[10, 10, 0, 0]} />
          <ComponentWithFetch crud={[10, 10, 0, 0]} />
          <ComponentWithFetch crud={[10, 10, 0, 0]} />
          <ComponentWithFetch crud={[10, 10, 0, 0]} />
        </div>
        <div className={styles.row}>
          <ComponentWithFetch crud={[10, 2, 0, 0]} />
          <ComponentWithFetch crud={[10, 2, 0, 0]} />
          <ComponentWithFetch crud={[10, 2, 0, 0]} />
          <ComponentWithFetch crud={[10, 2, 0, 0]} />
        </div>
      </main>
    </>
  )
}
